"""STUB: effect not implemented — do not guess mechanics.
Marowak δ (EX11 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import energy_bone_snipe, metal_crusher
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="058a7e77-5f89-509d-971f-1169c4714fb6",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name",
    display_name="Marowak δ",
    searchable_by=["Marowak \u03b4", "Stage 1", "Marowak"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIGHTING, PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=104,
    abilities=[
        Attack(
            title="Energy Bone",
            game_text="Choose a number of your opponent's Pok\u00e9mon up to the amount of Energy attached to Marowak. This attack does 20 damage to each of them.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            effect=energy_bone_snipe(20),
        ),
        Attack(
            title="Metal Crusher",
            game_text="If the Defending Pok\u00e9mon is Metal Pok\u00e9mon, this attack's base damage is 90.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=metal_crusher(50, 90),
        ),
    ],
)