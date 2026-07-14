from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import retreat_discount, is_in_active_spot

card = PokemonCardDef(
    guid="735e5851-e086-5a35-9884-6c632b8a286f",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSneasler.Name",
    display_name="Hisuian Sneasler",
    searchable_by=["Hisuian Sneasler", "Stage 1", "HisuianSneasler"],
    subtypes=["Stage 1"],
    collector_number=93,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSneasel.Name",
    family_id=215,
    abilities=[
        Ability(
            title="Carry and Climb",
            game_text="As long as this Pok\u00e9mon is on your Bench, your Active Pok\u00e9mon's Retreat Cost is ColorlessColorless less.",
            passive=retreat_discount(
                2,
                target_pred=lambda pokemon, carrier: (
                    pokemon.owning_player_id == carrier.owning_player_id
                    and is_in_active_spot(pokemon)
                    and not is_in_active_spot(carrier)
                ),
            ),
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)