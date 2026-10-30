from spirit.game.card_effects.ex import shock_bolt_discard_lightning, darkest_impulse_passive
"""STUB: effect not implemented — do not guess mechanics.
Dark Ampharos (EX7 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    passive=darkest_impulse_passive(),
    guid="6c5124fa-6544-5af2-9141-78afc587e22c",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkAmpharos.Name",
    display_name="Dark Ampharos",
    searchable_by=["Dark Ampharos", "Stage 2", "DarkAmpharos"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkFlaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Darkest Impulse",
            game_text="As long as Dark Ampharos is in play, whenever your opponent plays an Evolution card from his or her hand to evolve 1 of his or her Pok\u00e9mon, put 2 damage counters on that Pok\u00e9mon. You can't use more than 1 Darkest Impulse Pok\u00e9-Body each turn.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Shock Bolt",
            game_text="Discard all Lightning Energy attached to Dark Ampharos.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            # STUB: attack effect not implemented
            effect=shock_bolt_discard_lightning(),
        ),
    ],
)