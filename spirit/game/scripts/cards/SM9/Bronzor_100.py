from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm5 import EvolutionaryAdvantagePassive

card = PokemonCardDef(
    guid="207eb06d-7d65-5de1-a084-16aa2e76cf25",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    display_name="Bronzor",
    searchable_by=["Bronzor", "Basic", "Bronzor"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=436,
    abilities=[
        Ability(
            title="Evolutionary Advantage",
            game_text="If you go second, this Pok\u00e9mon can evolve during your first turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=EvolutionaryAdvantagePassive(),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)