from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


card = PokemonCardDef(
    guid="d396878e-d853-5394-b999-13a62b6076e1",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name",
    display_name="Swinub",
    searchable_by=["Swinub", "Basic", "Swinub"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=220,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Take Down",
            game_text="Swinub does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)
