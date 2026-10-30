"""STUB: effect not implemented — do not guess mechanics.
Forretress (EX10 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import spiky_shell_delayed, pop_forretress

card = PokemonCardDef(
    guid="5b605d23-b667-5d5a-8cf7-78aecd677596",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name",
    display_name="Forretress",
    searchable_by=["Forretress", "Stage 1", "Forretress"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Attack(
            title="Spiky Shell",
            game_text="Put 3 damage counters on the Defending Pok\u00e9mon at the end of your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=spiky_shell_delayed(3),
        ),
        Attack(
            title="Pop",
            game_text="Put 7 damage counters on Forretress. Move all Energy cards attached to Forretress to your Benched Pok\u00e9mon in any way you like. (Ignore this effect if you don't have any Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            # STUB: attack effect not implemented
            effect=pop_forretress(7),
        ),
    ],
)