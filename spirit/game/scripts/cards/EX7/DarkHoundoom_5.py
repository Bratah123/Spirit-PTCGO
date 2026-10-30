from spirit.game.card_effects.ex import shakedown_discard_hand, dark_fire
"""STUB: effect not implemented — do not guess mechanics.
Dark Houndoom (EX7 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e365b499-e1d0-5e72-ac90-d51236d1e47e",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkHoundoom.Name",
    display_name="Dark Houndoom",
    searchable_by=["Dark Houndoom", "Stage 1", "DarkHoundoom"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Shakedown",
            game_text="Choose a card from your opponent's hand without looking and discard it.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=shakedown_discard_hand(),
        ),
        Attack(
            title="Dark Fire",
            game_text="You may discard a Fire Energy or Darkness Energy attached to Dark Houndoom. If you do, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=dark_fire(),
        ),
    ],
)