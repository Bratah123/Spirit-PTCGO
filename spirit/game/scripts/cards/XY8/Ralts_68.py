from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="14012d52-253c-5874-9dcc-85d143bc4f3c",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    display_name="Ralts",
    searchable_by=["Ralts", "Basic", "Ralts"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=280,
    abilities=[
        Attack(
            title="Nap",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=heal_attack(30),
        ),
        Attack(
            title="Smack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)