from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import flip_tails_discard_energy, flip_reduce_damage_passive

card = PokemonCardDef(
    guid="3c8c873f-9227-5080-90be-0d971c529c0e",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="EX3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Sand Guard",
            game_text="Whenever Flygon would be damaged by your opponent's attack (after applying Weakness and Resistance), flip a coin. If heads, reduce that damage by 20.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=flip_reduce_damage_passive(20, title="Sand Guard"),
        ),
        Attack(
            title="Air Slash",
            game_text="Flip a coin. If tails, discard an Energy card attached to Flygon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=flip_tails_discard_energy(),
        ),
    ],
)