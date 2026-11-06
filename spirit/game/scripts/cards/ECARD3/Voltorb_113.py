from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="6db9d618-2d7b-5376-bd62-747436aadb4c",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    display_name="Voltorb",
    searchable_by=["Voltorb", "Basic", "Voltorb"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=100,
    abilities=[
        Attack(
            title="Magnetic Pull",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and switch it with the Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=gust_attack(damage_before=0),
        ),
        Attack(
            title="Spin Tackle",
            game_text="Voltorb does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)
