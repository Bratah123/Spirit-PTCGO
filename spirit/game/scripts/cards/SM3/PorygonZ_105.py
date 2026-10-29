from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm3 import initialize

card = PokemonCardDef(
    guid="ba2fcb87-7bdf-560b-bffb-a8f49a37436e",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2", "PorygonZ"],
    subtypes=["Stage 2"],
    collector_number=105,
    set_code="SM3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=137,
    abilities=[
        Ability(
            title="Initialize",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may devolve each of your opponent's evolved Pok\u00e9mon by putting the highest Stage Evolution card on it into your opponent's hand.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=initialize,
        ),
        Attack(
            title="Zap Cannon",
            game_text="This Pok\u00e9mon can't use Zap Cannon during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            locks_next_turn=True,
        ),
    ],
)
