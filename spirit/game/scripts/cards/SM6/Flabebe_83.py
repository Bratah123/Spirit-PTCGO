from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm5 import EvolutionaryAdvantagePassive

card = PokemonCardDef(
    guid="888a34f9-e88e-5cc5-8217-608e4028db7d",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flabebe.Name",
    display_name="Flabébé",
    searchable_by=["Flab\u00e9b\u00e9", "Basic", "Flabebe"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=669,
    abilities=[
        Ability(
            title="Evolutionary Advantage",
            game_text="If you go second, this Pok\u00e9mon can evolve during your first turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=EvolutionaryAdvantagePassive(),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
        ),
    ],
)
