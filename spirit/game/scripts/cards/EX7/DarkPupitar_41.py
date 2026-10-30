"""STUB: effect not implemented — do not guess mechanics.
Dark Pupitar (EX7 #41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, ignore_resistance_attack


card = PokemonCardDef(
    guid="a9ee1159-674e-517c-be7b-780be8e27f8a",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPupitar.Name",
    display_name="Dark Pupitar",
    searchable_by=["Dark Pupitar", "Stage 1", "DarkPupitar"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Dark Streak",
            game_text="Flip a coin. If heads, each Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage is not affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=ignore_resistance_attack(),
        ),
    ],
)