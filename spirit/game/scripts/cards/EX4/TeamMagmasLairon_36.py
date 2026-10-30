"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Lairon (EX4 #36): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import conditions_if

card = PokemonCardDef(
    guid="c35bab88-5ffb-5924-8e81-135a5ce3688a",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasLairon.Name",
    display_name="Team Magma's Lairon",
    searchable_by=["Team Magma's Lairon", "Stage 1", "TeamMagmasLairon"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasAron.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Land Sonic",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=conditions_if(lambda ctx: ctx.defender is not None and (ctx.max_hp(ctx.defender)-ctx.defender.get_attribute(AttrID.HP,0))//10>0, SpecialConditions.CONFUSED),
        ),
    ],
)