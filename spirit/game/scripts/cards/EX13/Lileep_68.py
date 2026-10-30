from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="0480319e-073e-5f7d-ac2c-18c1d7023b32",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    display_name="Lileep δ",
    searchable_by=["Lileep \u03b4", "Stage 1", "Lileep"],
    subtypes=["Stage 1"],
    collector_number=68,
    set_code="EX13",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RootFossil.Name",
    family_id=345,
    abilities=[
        Attack(
            title="Poison Tentacles",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)