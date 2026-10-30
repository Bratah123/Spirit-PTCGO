from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_item

card = PokemonCardDef(
    guid="5a517d14-698e-5674-a558-d9aec9ce784d",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    display_name="Dratini",
    searchable_by=["Dratini", "Basic", "Dratini"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    family_id=147,
    abilities=[
        Attack(
            title="Dragon Dew",
            game_text="Remove 2 damage counters from 1 of your Pok\u00e9mon (remove 1 if there is only 1).",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=heal_item(20, scope="choice"),
        ),
        Attack(
            title="Tail Slap",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)