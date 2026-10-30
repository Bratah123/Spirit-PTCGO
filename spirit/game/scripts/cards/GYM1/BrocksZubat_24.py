from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import alert, has_bench


card = PokemonCardDef(
    guid="62e7a0e0-5d1d-59d8-909a-3a405193531f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksZubat.Name",
    display_name="Brock's Zubat",
    searchable_by=["Brock's Zubat", "Basic", "BrocksZubat"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=41,
    abilities=[
        Attack(
            title="Alert",
            game_text="Draw a card. Then, switch Brock's Zubat with 1 of your Benched Pok\u00e9mon. You can't use this attack if your Bench is empty.",
            cost={PokemonTypes.COLORLESS: 1},
            condition=has_bench,
            effect=alert,
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
