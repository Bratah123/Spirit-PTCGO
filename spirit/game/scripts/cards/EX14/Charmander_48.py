from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import retaliate_damage

card = PokemonCardDef(
    guid="1a2c852c-5b49-5f4a-b764-317f6ec51488",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic", "Charmander"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="EX14",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Retaliate",
            game_text="Does 10 damage times the number of damage counters on Charmander.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
                        effect=retaliate_damage(10),
        ),
        Attack(
            title="Flame Tail",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)