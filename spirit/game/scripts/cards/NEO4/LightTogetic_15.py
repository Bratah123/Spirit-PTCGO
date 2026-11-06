from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import light_togetic_gift, sweet_kiss


card = PokemonCardDef(
    guid="0aef6db5-c560-5698-9550-43244bc51a68",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightTogetic.Name",
    display_name="Light Togetic",
    searchable_by=["Light Togetic", "Stage 1", "LightTogetic"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    family_id=175,
    abilities=[
        Ability(
            title="Gift",
            game_text="When you play Light Togetic from your hand, your opponent may search his or her deck for a Pok\u00e9mon Tool card, show that card to you, and put it into his or her hand. Either way, you may do the same, and then each player who searched shuffles his or her deck.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            effect=light_togetic_gift,
        ),
        Attack(
            title="Sweet Kiss",
            game_text="Your opponent may draw a card.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=sweet_kiss,
        ),
    ],
)
