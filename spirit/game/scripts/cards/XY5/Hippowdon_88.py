"""STUB: effect not implemented — do not guess mechanics.
Hippowdon (XY5 #88): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


card = PokemonCardDef(
    guid="d436ca01-6786-5374-9273-af463a7b5ddd",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippowdon.Name",
    display_name="Hippowdon",
    searchable_by=["Hippowdon", "Stage 1", "Hippowdon"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    family_id=449,
    abilities=[
        Attack(
            title="Resistance Desert",
            game_text="During your opponent's next turn, prevent all effects of attacks, including damage, done to this Pok\u00e9mon by Pok\u00e9mon-EX.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            # STUB: attack effect not implemented
            effect=recoil_attack(20),
        ),
    ],
)