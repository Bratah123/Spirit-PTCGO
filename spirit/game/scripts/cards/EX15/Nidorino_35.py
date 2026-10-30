"""STUB: effect not implemented — do not guess mechanics.
Nidorino δ (EX15 #35): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import rage_damage
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="01e3e85f-f58a-5d02-afb2-cbceaba838f6",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    display_name="Nidorino δ",
    searchable_by=["Nidorino \u03b4", "Stage 1", "Nidorino"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    family_id=33,
    abilities=[
        Attack(
            title="Rage",
            game_text="Does 10 damage plus 10 more damage for each damage counter on Nidorino.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=rage_damage(10, 10),
        ),
        Attack(
            title="Horn Drill",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)