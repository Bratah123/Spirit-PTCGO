"""Buizel (POP9 #6)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import may_discard_defender_energy_on_heads, partner_flip_full_protect


card = PokemonCardDef(
    guid="e66125e7-bae4-579a-a10f-6f090c6bf956",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name",
    display_name="Buizel",
    searchable_by=["Buizel", "Basic", "Buizel"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="POP9",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=418,
    abilities=[
        Attack(
            title="Whirlpool",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=may_discard_defender_energy_on_heads()
        ),
        Attack(
            title="Super Fast",
            game_text="If you have Pachirisu in play, flip a coin. If heads, prevent all effects of an attack, including damage, done to Buizel during your opponent's next turn.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=partner_flip_full_protect('Pachirisu')
        ),
    ]
)