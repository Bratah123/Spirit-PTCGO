from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import fireworks, has_typed_basic_energy


card = PokemonCardDef(
    guid="53994bf9-c393-5009-9e93-76724811e7df",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesCharmander.Name",
    display_name="Blaine's Charmander",
    searchable_by=["Blaine's Charmander", "Basic", "BlainesCharmander"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Fire Tail Slap",
            game_text="Use this attack only if there are any Fire Energy cards attached to Blaine's Charmander. Flip a coin. If tails, discard 1 of those cards.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            condition=has_typed_basic_energy(PokemonTypes.FIRE),
            effect=fireworks,
        ),
    ],
)
