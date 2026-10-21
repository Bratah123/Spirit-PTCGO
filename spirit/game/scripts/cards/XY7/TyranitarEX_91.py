from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage


card = PokemonCardDef(
    guid="440df31c-f4bc-57cd-bd97-ef1db004684f",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TyranitarEX.Name",
    display_name="Tyranitar-EX",
    searchable_by=["Tyranitar-EX", "Basic", "EX", "TyranitarEX"],
    subtypes=["Basic", "EX"],
    collector_number=91,
    set_code="XY7",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=248,
    abilities=[
        Attack(
            title="Hammer In",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Break Ground",
            game_text="This attack does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=spread_damage(10, side='mine', also_base=True),
        ),
    ],
)