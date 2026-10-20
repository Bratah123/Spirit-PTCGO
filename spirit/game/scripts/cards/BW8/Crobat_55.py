from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="ff0fdd93-db6f-5692-96c5-907745a63505",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2", "Team Plasma", "Crobat"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=55,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Night Sight",
            game_text="Once during your turn (before your attack), you may draw a card.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Ultra-Toxic Fang",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Put 4 damage counters instead of 1 on this Pok\u00e9mon between turns.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)