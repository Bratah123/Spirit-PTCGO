from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="3f0add16-1668-56c8-b576-59975d8a5f1c",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name",
    display_name="Skrelp",
    searchable_by=["Skrelp", "Basic", "Skrelp"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=690,
    abilities=[
        Attack(
            title="Spit Poison",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)