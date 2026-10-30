"""STUB: effect not implemented — do not guess mechanics.
Infernape LV.X (DPP #DP10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="48a532f7-c721-5c49-ac06-141d1395b4fa",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.InfernapeLVX.Name",
    display_name="Infernape LV.X",
    searchable_by=["Infernape LV.X", "Level-Up", "InfernapeLVX"],
    subtypes=["Level-Up"],
    collector_number=10,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.LEVELUP,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name",
    family_id=392,
    abilities=[
        Ability(
            title="Burning Head",
            game_text="Once during your turn (before your attack), you may look at the top 3 cards of your deck, choose 1 of them, and put it into your hand. Discard the other 2 cards. This power can't be used if Infernape is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flare Up",
            game_text="Search your discard pile for 8 Fire Energy cards, show them to your opponent, and shuffle them into your deck. (This attack does nothing if you don't have 8 Fire Energy cards in your discard pile.)",
            cost={PokemonTypes.FIRE: 2},
            damage=150,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)