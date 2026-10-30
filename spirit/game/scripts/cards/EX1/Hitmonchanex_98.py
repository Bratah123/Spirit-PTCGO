from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, ignore_resistance_attack


card = PokemonCardDef(
    guid="86ead38f-ab05-59ad-a84c-c883884f3846",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchanex.Name",
    display_name="Hitmonchan ex",
    searchable_by=["Hitmonchan ex", "Basic", "ex", "Hitmonchanex"],
    subtypes=["Basic", "ex"],
    collector_number=98,
    set_code="EX1",
    rarity=Rarities.RareHoloEX,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=107,
    abilities=[
        Attack(
            title="Steady Punch",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
        Attack(
            title="Sky Uppercut",
            game_text="This attack's damage is not affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ignore_resistance_attack(),
        ),
    ],
)
