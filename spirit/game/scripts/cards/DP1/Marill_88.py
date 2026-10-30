"""STUB: effect not implemented — do not guess mechanics.
Marill (DP1 #88): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import bonus_if_evolved_from
from spirit.game.card_effects.dp import splashing_turn

card = PokemonCardDef(
    guid="e26cd732-c383-5e29-8cdf-b476117a89e3",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    display_name="Marill",
    searchable_by=["Marill", "Basic", "Marill"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="DP1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=183,
    abilities=[
        Attack(
            title="Rollout",
            game_text="If Marill is evolved from Azurill, this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if_evolved_from('Azurill', bonus=20, base=10),
        ),
        Attack(
            title="Splashing Turn",
            game_text="Switch Marill with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            effect=splashing_turn(),
        ),
    ],
)