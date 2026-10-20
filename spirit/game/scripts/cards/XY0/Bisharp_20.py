from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="9953174a-de24-5f33-83fe-adf6c64c9542",
    key="XY0",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    display_name="Bisharp",
    searchable_by=["Bisharp", "Stage 1", "Bisharp"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="XY0",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    family_id=624,
    abilities=[
        Attack(
            title="Wicked Jab",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)