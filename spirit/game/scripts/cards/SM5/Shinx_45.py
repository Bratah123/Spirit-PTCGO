from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm5 import EvolutionaryAdvantagePassive

card = PokemonCardDef(
    guid="ac25c3e2-e256-5137-9895-6a7019a514f7",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    display_name="Shinx",
    searchable_by=["Shinx", "Basic", "Shinx"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=403,
    abilities=[
        Ability(
            title="Evolutionary Advantage",
            game_text="If you go second, this Pok\u00e9mon can evolve during your first turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=EvolutionaryAdvantagePassive(),
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)