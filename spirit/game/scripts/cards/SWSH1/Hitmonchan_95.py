from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, named_in_play

card = PokemonCardDef(
    guid="18ac4b65-9532-5b79-abfb-4122e9a3a7ae",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchan.Name",
    display_name="Hitmonchan",
    searchable_by=["Hitmonchan", "Basic", "Hitmonchan"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=107,
    abilities=[
        Attack(
            title="Coordinated Beatdown",
            game_text="If Hitmonlee is on your Bench, this attack does 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(named_in_play("Hitmonlee"), 20, base=20),
        ),
        Attack(
            title="Mach Cross",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
        ),
    ],
)