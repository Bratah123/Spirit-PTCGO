from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="d156616f-b9e3-5c71-a09f-027083e5ae4a",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name",
    display_name="Tentacruel",
    searchable_by=["Tentacruel", "Stage 1", "Tentacruel"],
    subtypes=["Stage 1"],
    collector_number=66,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    family_id=72,
    abilities=[
        Attack(
            title="Supersonic",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Jellyfish Sting",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.WATER: 2},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
