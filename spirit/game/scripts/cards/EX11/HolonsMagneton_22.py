"""STUB: effect not implemented — do not guess mechanics.
Holon's Magneton (EX11 #22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import extra_ball_vs_ex
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a568645-190a-5268-8fa4-28e59b91e31d",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HolonsMagneton.Name",
    display_name="Holon's Magneton",
    searchable_by=["Holon's Magneton", "Stage 1", "HolonsMagneton"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HolonsMagnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Extra Ball",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=extra_ball_vs_ex(30, 20),
        ),
    ],
)