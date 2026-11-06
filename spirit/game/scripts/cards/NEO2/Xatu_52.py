from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import energy_cycle


card = PokemonCardDef(
    guid="1c62ca92-0fbe-555a-8471-2ffe9046b56f",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name="Xatu",
    searchable_by=["Xatu", "Stage 1", "Xatu"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=177,
    abilities=[
        Attack(
            title="Energy Cycle",
            game_text="Flip a coin. If heads, choose 1 Energy card attached to the Defending Pok\u00e9mon and 1 of your opponent's Benched Pok\u00e9mon. Attach that Energy card to that Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=energy_cycle,
        ),
        Attack(
            title="Super Psy",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
