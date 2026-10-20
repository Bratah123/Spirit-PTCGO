from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="98dfccbd-54a7-5347-9c8e-3da380b572a2",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name",
    display_name="Bergmite",
    searchable_by=["Bergmite", "Basic", "Bergmite"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=712,
    abilities=[
        Attack(
            title="Ice Block",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=heal_attack(30),
        ),
        Attack(
            title="Icy Snow",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)