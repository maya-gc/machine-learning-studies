# data/dataset.py

import random

NOMES = [
    "Ana", "Bruno", "Carla", "Diego", "Eduarda", "Felipe", "Gabriela",
    "Henrique", "Isabela", "João", "Larissa", "Marcos", "Natália", "Paulo"
]

EMPRESAS = [
    "TechNova", "Alfa Sistemas", "DeltaLog", "InovaCorp", "BlueData",
    "Mercato", "FinPlus", "EduSmart", "Nexa", "Prime Office"
]

DOMINIOS = [
    "portal-ofertas.com",
    "seguranca-conta.net",
    "premio-agora.org",
    "empresa.com.br",
    "intranet.local",
    "suporte-servico.com",
    "financeiro-interno.com.br"
]

VALORES = ["50", "100", "200", "500", "1000", "2500"]
DATAS = ["hoje", "amanhã", "nesta semana", "até sexta-feira", "até o fim do mês"]
AREAS = ["projeto", "financeiro", "comercial", "suporte", "marketing", "RH", "TI"]

SPAM_TEMPLATES = [
    "Parabéns {nome}, você ganhou um prêmio de R$ {valor}",
    "Oferta exclusiva para {nome}: compre agora e receba {valor}% de desconto",
    "Clique no link http://{dominio} para liberar seu benefício",
    "Sua conta será bloqueada hoje, acesse http://{dominio} para regularizar",
    "Ganhe dinheiro trabalhando de casa a partir de hoje",
    "Promoção válida somente {data}, aproveite antes que acabe",
    "Você foi selecionado para receber um voucher especial",
    "Última chance de participar do sorteio de R$ {valor}",
    "Atualize seus dados imediatamente em http://{dominio}",
    "Seu cadastro foi premiado com bônus exclusivo",
    "Atenção {nome}: identificamos atividade suspeita, confirme sua conta agora",
    "Pagamento pendente encontrado, clique para evitar cancelamento",
    "Receba comissão rápida sem experiência, inscrição aberta",
    "Crédito aprovado para você sem consulta ao SPC",
    "Seu pacote foi retido, pague a taxa de liberação agora",
    "Convite VIP para promoção secreta com vagas limitadas",
    "Você acaba de ganhar acesso premium gratuito",
    "Oferta relâmpago de investimento com retorno garantido",
    "Seu reembolso está disponível, informe seus dados bancários",
    "Campanha especial para clientes selecionados com prêmio instantâneo"
]

HAM_TEMPLATES = [
    "Reunião do time de {area} confirmada para {data}",
    "Segue em anexo o relatório atualizado do setor de {area}",
    "{nome}, precisamos revisar o cronograma do projeto nesta semana",
    "Confirmação de presença no evento interno da {empresa}",
    "Atualização do status das entregas do time de {area}",
    "Envio do relatório final para análise da gerência",
    "Solicitação de feedback sobre a apresentação enviada ontem",
    "Agendamento de reunião com a equipe da {empresa}",
    "Compartilhando as fotos do encontro da equipe",
    "Aviso de manutenção programada no sistema interno",
    "Documento para aprovação referente ao orçamento mensal",
    "Resumo da reunião de alinhamento do projeto",
    "Pedido de revisão do material técnico enviado por e-mail",
    "Informamos que o treinamento de {area} ocorrerá {data}",
    "{nome}, segue a atualização das tarefas sob sua responsabilidade",
    "Convite para participar do workshop promovido pela {empresa}",
    "Confirmação do recebimento da documentação enviada",
    "Mudança no horário da reunião com o cliente",
    "Atualização do cronograma de implantação do sistema",
    "Mensagem de acompanhamento sobre o atendimento realizado"
]

SPAM_VARIACOES = [
    "",
    " Resposta imediata necessária.",
    " Não perca esta oportunidade.",
    " Ação urgente.",
    " Vagas limitadas.",
    " Promoção por tempo limitado."
]

HAM_VARIACOES = [
    "",
    " Obrigado.",
    " Fico no aguardo.",
    " Qualquer dúvida, me avise.",
    " Atenciosamente.",
    " Para sua conferência."
]

def preencher(template):
    return template.format(
        nome=random.choice(NOMES),
        empresa=random.choice(EMPRESAS),
        dominio=random.choice(DOMINIOS),
        valor=random.choice(VALORES),
        data=random.choice(DATAS),
        area=random.choice(AREAS)
    )

def gerar_exemplos(templates, variacoes, quantidade):
    exemplos = []
    for _ in range(quantidade):
        base = preencher(random.choice(templates))
        variacao = random.choice(variacoes)
        exemplos.append((base + variacao).strip())
    return exemplos

def load_data(num_spam=400, num_ham=400, seed=42):
    random.seed(seed)

    spam_emails = gerar_exemplos(SPAM_TEMPLATES, SPAM_VARIACOES, num_spam)
    ham_emails = gerar_exemplos(HAM_TEMPLATES, HAM_VARIACOES, num_ham)

    emails = spam_emails + ham_emails
    labels = [1] * len(spam_emails) + [0] * len(ham_emails)

    combinado = list(zip(emails, labels))
    random.shuffle(combinado)

    emails, labels = zip(*combinado)
    return list(emails), list(labels)