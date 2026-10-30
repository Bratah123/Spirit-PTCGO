from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import smokescreen_attack
from spirit.game.card_effects.ex import flip_tails_discard_energy


card = PokemonCardDef(
    guid="13f8cb8e-857e-5b85-8ab4-31084bc46231",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    display_name="Charmeleon",
    searchable_by=["Charmeleon", "Stage 1", "Charmeleon"],
    subtypes=["Stage 1"],
    collector_number=99,
    set_code="EX3",
    rarity=Rarities.RareSecret,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Smokescreen",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=smokescreen_attack(),
        ),
        Attack(
            title="Fireworks",
            game_text="Flip a coin. If tails, discard a Fire Energy card attached to Charmeleon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=flip_tails_discard_energy(PokemonTypes.FIRE),
        ),
    ],
)