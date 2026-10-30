from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import false_charity


card = PokemonCardDef(
    guid="d5743de5-b474-5905-96a7-0526f640f853",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisMeowth.Name",
    display_name="Giovanni's Meowth",
    searchable_by=["Giovanni's Meowth", "Basic", "GiovannisMeowth"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=52,
    abilities=[
        Attack(
            title="False Charity",
            game_text="Flip a coin. If heads, look at the top card of your opponent's deck. If it's a Trainer card, put it in your opponent's discard pile; otherwise, put it into his or her hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=false_charity,
        ),
        Attack(
            title="Double Scratch",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=20),
        ),
    ],
)
