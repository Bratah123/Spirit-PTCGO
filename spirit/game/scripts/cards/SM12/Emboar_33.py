from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import explosive_fire_dance

card = PokemonCardDef(
    guid="74d642b2-9344-5bc4-8e8e-f32f77fe4d28",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Emboar.Name",
    display_name="Emboar",
    searchable_by=["Emboar", "Stage 2", "Emboar"],
    subtypes=["Stage 2"],
    collector_number=33,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name",
    family_id=498,
    abilities=[
        Ability(
            title="Explosive Fire Dance",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may look at the top 8 cards of your deck and attach any number of basic Energy cards you find there to your Pok\u00e9mon in any way you like. Shuffle the other cards back into your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=explosive_fire_dance,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
        ),
    ],
)