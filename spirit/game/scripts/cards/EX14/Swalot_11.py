from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import pick_and_choose_conditions, reactive_poison

card = PokemonCardDef(
    guid="c9f936d2-40fb-58e5-8638-89fcc36b204f",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swalot.Name",
    display_name="Swalot",
    searchable_by=["Swalot", "Stage 1", "Swalot"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="EX14",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gulpin.Name",
    family_id=316,
    abilities=[
        Attack(
            title="Pick and Choose",
            game_text="Choose either Burned or Poisoned, and either Asleep or Confused. The Defending Pok\u00e9mon is now affected by both Special Conditions.",
            cost={PokemonTypes.COLORLESS: 2},
                        effect=pick_and_choose_conditions(),
        ),
        Attack(
            title="Reactive Poison",
            game_text="Does 50 damage plus 20 more damage for each Special Condition affecting the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
                        effect=reactive_poison(50, 20),
        ),
    ],
)