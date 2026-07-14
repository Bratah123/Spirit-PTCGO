from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy

card = PokemonCardDef(
    guid="c39d5335-b23a-5bb9-bb92-3d6392c947d7",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoV.Name",
    display_name="Tapu Koko V",
    searchable_by=["Tapu Koko V", "Basic", "V", "TapuKokoV"],
    subtypes=["Basic", "V"],
    collector_number=50,
    set_code="SWSH5",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=785,
    abilities=[
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
        ),
        Attack(
            title="Spiral Thunder",
            game_text="This attack does 40 more damage for each Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_energy("opponent"), 40, base=20),
        ),
    ],
)