"""STUB: effect not implemented — do not guess mechanics.
Bibarel (DP1 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import rest_attack
from spirit.game.card_effects.dp import recoil_attack

card = PokemonCardDef(
    guid="f3aa4727-3a39-5e65-ae26-e3d7b64fb232",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bibarel.Name",
    display_name="Bibarel",
    searchable_by=["Bibarel", "Stage 1", "Bibarel"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name",
    family_id=399,
    abilities=[
        Attack(
            title="Rest",
            game_text="Remove all Special Conditions and 4 damage counters from Bibarel. Bibarel is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=rest_attack(4),
        ),
        Attack(
            title="Take Down",
            game_text="Bibarel does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=recoil_attack(10),
        ),
    ],
)