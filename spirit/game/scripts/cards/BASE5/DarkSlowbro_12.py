from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ecard import reel_in


card = PokemonCardDef(
    guid="b0d59cb5-aaa7-5f0e-8b2c-b61888b0ebc4",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkSlowbro.Name",
    display_name="Dark Slowbro",
    searchable_by=["Dark Slowbro", "Stage 1", "DarkSlowbro"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Reel In",
            game_text="When you play Dark Slowbro from your hand, choose up to 3 Basic Pok\u00e9mon and/or Evolution cards from your discard pile and put them into your hand.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            effect=reel_in,
        ),
        Attack(
            title="Fickle Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=40,
            effect=flip_or_nothing(),
        ),
    ],
)
