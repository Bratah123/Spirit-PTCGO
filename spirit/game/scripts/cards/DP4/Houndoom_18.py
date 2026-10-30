"""STUB: effect not implemented — do not guess mechanics.
Houndoom (DP4 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import knock_off_random_hand


card = PokemonCardDef(
    guid="5f66d68b-775a-5410-826b-8fc06d387cd1",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Houndoom"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="DP4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Dark Fang",
            game_text="Choose 1 card from your opponent's hand without looking and discard it.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=knock_off_random_hand(),
        ),
        Attack(
            title="Black Fire",
            game_text="You may discard a Fire or Darkness Energy attached to Houndoom. If you discard a Fire Energy, the Defending Pok\u00e9mon is now Burned. If you discard a Darkness Energy, this attack does 40 damage plus 30 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)