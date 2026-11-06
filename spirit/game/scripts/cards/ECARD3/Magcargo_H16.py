from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import eruption, fire_stream, has_typed_basic_energy


card = PokemonCardDef(
    guid="fc6d3b47-7a0b-5ab3-86ef-fa4e688293ee",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name",
    display_name="Magcargo",
    searchable_by=["Magcargo", "Stage 1", "Magcargo"],
    subtypes=["Stage 1"],
    collector_number=166,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Attack(
            title="Eruption",
            game_text="Each player discard the top card of his or her deck. This attack does 20 damage plus 20 more damage for each Fire Energy card discarded in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=eruption,
        ),
        Attack(
            title="Fire Stream",
            game_text="Discard a Fire Energy card attached to Magcargo in order to use this attack. If your opponent has any Benched Pok\u00e9mon, this attack does 10 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            condition=has_typed_basic_energy(PokemonTypes.FIRE),
            effect=fire_stream,
        ),
    ],
)
