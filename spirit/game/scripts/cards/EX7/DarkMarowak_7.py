from spirit.game.card_effects.ex import brick_smash, hard_bone_discard_pokemon
"""STUB: effect not implemented — do not guess mechanics.
Dark Marowak (EX7 #7): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0f0ec8a3-b7ec-5111-8d25-9625c412129b",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkMarowak.Name",
    display_name="Dark Marowak",
    searchable_by=["Dark Marowak", "Stage 1", "DarkMarowak"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIGHTING, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=104,
    abilities=[
        Attack(
            title="Brick Smash",
            game_text="This attack's damage isn't affected by Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=brick_smash(),
        ),
        Attack(
            title="Hard Bone",
            game_text="Discard a Basic Pok\u00e9mon or Evolution card from your hand or this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            # STUB: attack effect not implemented
            effect=hard_bone_discard_pokemon(),
        ),
    ],
)