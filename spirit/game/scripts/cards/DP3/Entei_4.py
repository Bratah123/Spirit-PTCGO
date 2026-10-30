"""STUB: effect not implemented — do not guess mechanics.
Entei (DP3 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="fb3624e6-32ed-5631-9741-8ca4fff05712",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic", "Entei"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Ability(
            title="Burning Coat",
            game_text="Whenever 1 of your opponent's Pok\u00e9mon is Knocked Out by damage from Entei's attacks, discard the top 3 cards from your opponent's deck.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Blaze Roar",
            game_text="Does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Flip a coin. If tails, discard 2 Fire Energy attached to Entei.",
            cost={PokemonTypes.FIRE: 3},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)