from spirit.game.card_effects.ex import gift_exchange, souvenir_flip3
"""STUB: effect not implemented — do not guess mechanics.
Delibird (EX7 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="2e38d6e3-809c-5a11-b35b-26cbbf33bf82",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name",
    display_name="Delibird",
    searchable_by=["Delibird", "Basic", "Delibird"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="EX7",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=225,
    abilities=[
        Ability(
            title="Gift Exchange",
            game_text="Once during your turn (before your attack), if Delibird is your Active Pok\u00e9mon, you may shuffle 1 card from your hand into your deck. Then, draw a card. This power can't be used if Delibird is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=gift_exchange(),
        ),
        Attack(
            title="Souvenir",
            game_text="Flip 3 coins. If 1 of them is heads, put 4 damage counters on the Defending Pok\u00e9mon. If 2 of them are heads, remove 1 damage counter from the Defending Pok\u00e9mon. If all of them are heads, put 10 damage counters on the Defending Pok\u00e9mon. If all of them are tails, remove all damage counters from the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=souvenir_flip3(),
        ),
    ],
)