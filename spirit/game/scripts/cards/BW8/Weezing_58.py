from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="708b2bb5-1a8f-5ae8-bf2e-2644c26fd7a1",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1", "Team Plasma", "Weezing"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=58,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Ability(
            title="Aftermath",
            game_text="When this Pok\u00e9mon is Knocked Out by damage from an opponent's attack, discard the top 3 cards of your opponent's deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Smogbank",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)