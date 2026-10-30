from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="92828325-d385-567d-9eb2-5fd3a9e661ae",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    display_name="Kabuto δ",
    searchable_by=["Kabuto \u03b4", "Stage 1", "Kabuto"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="EX13",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=140,
    abilities=[
        Attack(
            title="Eerie Light",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Shell Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)