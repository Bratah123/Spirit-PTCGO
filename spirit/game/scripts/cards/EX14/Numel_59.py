from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import take_down_recoil

card = PokemonCardDef(
    guid="3d91cf58-726f-5f2f-a9c3-0fbbbe0818b0",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    display_name="Numel",
    searchable_by=["Numel", "Basic", "Numel"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="EX14",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=322,
    abilities=[
        Attack(
            title="Take Down",
            game_text="Numel does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
                        effect=take_down_recoil(10),
        ),
    ],
)