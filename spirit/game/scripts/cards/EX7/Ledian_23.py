from spirit.game.card_effects.ex import powder_protection_passive
"""STUB: effect not implemented — do not guess mechanics.
Ledian (EX7 #23): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    passive=powder_protection_passive(),
    guid="532b93ca-32e8-5e19-ab12-3652a37f148f",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ledian.Name",
    display_name="Ledian",
    searchable_by=["Ledian", "Stage 1", "Ledian"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="EX7",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name",
    family_id=165,
    abilities=[
        Ability(
            title="Powder Protection",
            game_text="Any damage done to Ledian by attacks from Pok\u00e9mon that has an owner in its name is reduced by 40.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Split Spiral Punch",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)